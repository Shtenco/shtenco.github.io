const state={lifecycle:"ALL",domain:"ALL",visibility:"ALL",search:"",flagshipOnly:false,lang:"ru"};
let allRepositories=[];

async function loadRepositories(){
  const response=await fetch("data/repositories.json",{cache:"no-store"});
  if(!response.ok) throw new Error("Repository data unavailable");
  const data=await response.json();
  return data.repositories;
}

function deriveMetrics(repositories){
  return {
    total:repositories.length,
    public:repositories.filter(r=>r.visibility==="public").length,
    private:repositories.filter(r=>r.visibility==="private").length,
    canonical:repositories.filter(r=>r.lifecycle==="CANONICAL").length,
    candidate:repositories.filter(r=>r.lifecycle==="CANDIDATE").length,
    research:repositories.filter(r=>r.lifecycle==="R&D").length
  };
}

function filterRepositories(repositories,currentState=state){
  const q=currentState.search.trim().toLowerCase();
  return repositories.filter(repo=>{
    if(currentState.lifecycle!=="ALL"&&repo.lifecycle!==currentState.lifecycle)return false;
    if(currentState.domain!=="ALL"&&repo.domain!==currentState.domain)return false;
    if(currentState.visibility!=="ALL"&&repo.visibility!==currentState.visibility)return false;
    if(currentState.flagshipOnly&&!repo.flagship)return false;
    if(q){
      const hay=[repo.name,repo.role_ru,repo.role_en,repo.domain,repo.kind,repo.lifecycle].join(" ").toLowerCase();
      if(!hay.includes(q))return false;
    }
    return true;
  });
}

function esc(value){return String(value??"").replace(/[&<>"']/g,ch=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[ch]));}

function localized(repo,field){
  const key=state.lang==="en"?field+"_en":field+"_ru";
  return repo[key]||repo[field+"_en"]||repo[field+"_ru"]||"";
}

function renderRepositoryCard(repo){
  const source=repo.public_url
    ? `<a class="repo-link" href="${esc(repo.public_url)}" target="_blank" rel="noopener noreferrer">GitHub ↗</a>`
    : '<span class="repo-private">PRIVATE / INTERNAL</span>';
  const successor=repo.canonical_successor
    ? `<span class="kind-badge">→ ${esc(repo.canonical_successor)}</span>`
    :"";
  const maturity=repo.maturity?`<span class="kind-badge">${esc(repo.maturity)}</span>`:"";
  return `<article class="repo-card">
    <div class="repo-top"><div class="repo-name">${esc(repo.name)}</div><span class="status-badge" data-status="${esc(repo.lifecycle)}">${esc(repo.lifecycle)}</span></div>
    <p class="repo-role">${esc(localized(repo,"role"))}</p>
    <div class="repo-meta"><span class="kind-badge">${esc(repo.domain)}</span><span class="kind-badge">${esc(repo.kind)}</span><span class="privacy-badge">${esc(repo.visibility)}</span>${maturity}${successor}</div>
    <p class="repo-boundary">${esc(localized(repo,"claim_boundary"))}</p>
    <div class="repo-footer">${source}<span class="kind-badge">${repo.flagship?"FLAGSHIP":"REGISTRY"}</span></div>
  </article>`;
}

function renderRegistry(repositories){
  const root=document.querySelector("#registry-grid");
  const count=document.querySelector("#registry-count");
  if(!root)return;
  const filtered=filterRepositories(repositories);
  if(count)count.textContent=String(filtered.length);
  root.innerHTML=filtered.length?filtered.map(renderRepositoryCard).join(""):'<div class="empty-state">No repositories match the selected filters.</div>';
}

function renderFlagships(repositories){
  const root=document.querySelector("#flagship-grid");
  if(!root)return;
  root.innerHTML=repositories.filter(r=>r.flagship).map(renderRepositoryCard).join("");
}

function renderDomainCollections(repositories){
  const tradingNames=new Set(["quantum-trading_metatrader5","computer_vision_trading_metatrader_5","swap_arbitrage_metatrader_5","cross_forex_arbitrage_trading_metatrader_5","global_liquidity_dataminer","3D_bars_market_structure","multi_threaded_trading_robot_with_machine_learning_python","midas_ai_trading_system","midas_lite","ai_trade_terminal","algotrading_graph_system","crypto_pump","synergy_agi_trader","midas_ai"]);
  const researchNames=new Set(["binary_quantum_theory","cold_nuclear","dlp_solver","motherboard_xpu_xml","qr_compress","agi_olga","synergy_matrix_sota","synergy_graph_print_money"]);
  const productNames=new Set(["synergy_app","synergy_messenger","ai_language","synergychain","synergychain.github.io","shtencoauantai.github.io"]);
  const render=(id,set)=>{const el=document.querySelector(id);if(el)el.innerHTML=repositories.filter(r=>set.has(r.name)).map(renderRepositoryCard).join("");};
  render("#lineage-grid",tradingNames);render("#research-grid",researchNames);render("#products-grid",productNames);
}

function renderMetrics(repositories){
  const m=deriveMetrics(repositories);
  Object.entries(m).forEach(([key,value])=>{document.querySelectorAll(`[data-metric="${key}"]`).forEach(el=>el.textContent=String(value));});
}

function syncLanguage(){
  document.body.dataset.lang=state.lang;
  document.documentElement.lang=state.lang;
  document.querySelectorAll("[data-lang-btn]").forEach(btn=>btn.setAttribute("aria-pressed",String(btn.dataset.langBtn===state.lang)));
  renderFlagships(allRepositories);renderDomainCollections(allRepositories);renderRegistry(allRepositories);
}

function wireFilters(){
  document.querySelectorAll("[data-lifecycle]").forEach(btn=>btn.addEventListener("click",()=>{state.lifecycle=btn.dataset.lifecycle;document.querySelectorAll("[data-lifecycle]").forEach(b=>b.setAttribute("aria-pressed",String(b===btn)));renderRegistry(allRepositories);}));
  document.querySelectorAll("[data-visibility]").forEach(btn=>btn.addEventListener("click",()=>{state.visibility=btn.dataset.visibility;document.querySelectorAll("[data-visibility]").forEach(b=>b.setAttribute("aria-pressed",String(b===btn)));renderRegistry(allRepositories);}));
  document.querySelectorAll("[data-domain]").forEach(btn=>btn.addEventListener("click",()=>{state.domain=btn.dataset.domain;document.querySelectorAll("[data-domain]").forEach(b=>b.setAttribute("aria-pressed",String(b===btn)));renderRegistry(allRepositories);}));
  const search=document.querySelector("#repo-search");if(search)search.addEventListener("input",e=>{state.search=e.target.value;renderRegistry(allRepositories);});
  const flagship=document.querySelector("#flagship-only");if(flagship)flagship.addEventListener("click",()=>{state.flagshipOnly=!state.flagshipOnly;flagship.setAttribute("aria-pressed",String(state.flagshipOnly));renderRegistry(allRepositories);});
  document.querySelectorAll("[data-lang-btn]").forEach(btn=>btn.addEventListener("click",()=>{state.lang=btn.dataset.langBtn;syncLanguage();}));
}

async function boot(){
  try{
    allRepositories=await loadRepositories();
    renderMetrics(allRepositories);
    renderFlagships(allRepositories);
    renderDomainCollections(allRepositories);
    renderRegistry(allRepositories);
    wireFilters();
    syncLanguage();
  }catch(error){
    console.error(error);
    const grid=document.querySelector("#registry-grid");
    if(grid)grid.innerHTML='<div class="empty-state">Repository registry could not be loaded. Static flagship content remains available.</div>';
  }
}

document.addEventListener("DOMContentLoaded",boot);
