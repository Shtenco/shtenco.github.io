# Portfolio Audit — target 79 / observed 77

Дата аудита: 2026-10-03

## Scope

- Пользовательский целевой счёт: **79 репозиториев**.
- GitHub connector на момент аудита возвращает **77 owned repositories**; запрос с offset=77 возвращает пустой результат.
- Канонический SYNERGY registry от 2026-09-28 содержит **75** репозиториев.
- Два новых доступных репозитория вне старого атласа: `synergy_complex_matrix_multiplication` и `synergy_computing_topology`.
- Позиции **78–79** не видны подключённому GitHub, поэтому их названия/содержание не выдумываются.

## Метод

Для 75 старых репозиториев использованы canonical atlas/registry, federation backlog, documentation-quality registry и security blockers. Для ключевых flagship-кандидатов и двух новых репозиториев выполнена прямая повторная проверка текущих README/evidence. Это **portfolio-level engineering audit**, а не утверждение, что каждая строка кода 77 репозиториев независимо переверифицирована.

## Portfolio tiers

- **FLAGSHIP** — полноценный подробный кейс.
- **STRONG** — полноценная карточка в Engineering Atlas.
- **SUPPORTING** — краткая карточка как часть системного семейства.
- **CONCEPT** — показывать только как R&D/архитектурную гипотезу.
- **SURFACE** — интерфейс/витрина, не выдавать за core runtime.
- **HOLD** — не продвигать в HR-верхний уровень до устранения проблемы или из-за слабой релевантности.

## Сводка

- 77 доступных: 21 FLAGSHIP, 21 STRONG, 12 SUPPORTING, 16 CONCEPT, 3 SURFACE, 4 HOLD.
- Старые 75: 42 federation-integrated; 33 с явными backlog/maturity ограничениями.
- Security HOLD: `synergy_usds`, `synergy_cashero`; `synergy_turbo_linux` требует credential review.

## Полная матрица

### Trading & Market Intelligence

| # | Repository | Что это / какую компетенцию показывает | Maturity | Evidence | Visibility | Tier | Рекомендация |
|---:|---|---|---|---|---|---|---|
| 1 | `3D_bars_market_structure` | Многомерные рыночные признаки и 3D-визуализация структуры рынка. | EXTERNAL_RUNTIME_PENDING | DIRECT_REVIEW | public | **STRONG** | Полная карточка в Engineering Atlas |
| 2 | `computer_vision_trading_metatrader_5` | Компьютерное зрение для визуального представления рыночных временных рядов. | EXTERNAL_RUNTIME_PENDING | DIRECT_REVIEW | public | **STRONG** | Полная карточка в Engineering Atlas |
| 3 | `cross_forex_arbitrage_trading_metatrader_5` | Cross-FX/synthetic-rate анализ и поиск ценовых расхождений. | EXTERNAL_RUNTIME_PENDING | DIRECT_REVIEW | public | **STRONG** | Полная карточка в Engineering Atlas |
| 4 | `global_liquidity_dataminer` | Сбор макроликвидности и объединение macro/market data для ML-исследований. | EXTERNAL_RUNTIME_PENDING | DIRECT_REVIEW | public | **STRONG** | Полная карточка в Engineering Atlas |
| 5 | `midas_lite` | Облегченная исследовательская ветка MIDAS и торговые прототипы. | EXTERNAL_RUNTIME_PENDING | DOC_VERIFIED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 6 | `multi_threaded_trading_robot_with_machine_learning_python` | Многопоточный ML trading pipeline с портфельным риск-контролем и MT5. | EXTERNAL_RUNTIME_PENDING | DIRECT_REVIEW | public | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 7 | `quantum-trading_metatrader5` | Ранний quantum-assisted trading prototype на Qiskit + MT5. | EXTERNAL_RUNTIME_PENDING | DIRECT_REVIEW | public | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 8 | `swap_arbitrage_metatrader_5` | Carry/swap-aware портфельная оптимизация и синтетические FX-портфели. | EXTERNAL_RUNTIME_PENDING | DIRECT_REVIEW | public | **STRONG** | Полная карточка в Engineering Atlas |
| 9 | `synergy_adaptive_engine` | Адаптивное переключение режимов, параметров и политик по состоянию рынка. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 10 | `synergy_agi_trader` | Reasoning/AI trader под независимыми риск-ограничениями. | EXTERNAL_RUNTIME_PENDING | REGISTRY_BASED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 11 | `synergy_ai_investment_committee` | AI investment committee: агрегация исследований и ограниченное принятие решений. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 12 | `synergy_ai_trade_terminal` | Терминал управления AI/algorithmic trading workloads. | EXTERNAL_RUNTIME_PENDING | REGISTRY_BASED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 13 | `synergy_algotrading_graph_system` | Графовая модель торговых состояний, маршрутов и взаимосвязей. | DOCUMENTATION_ONLY | DOC_VERIFIED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 14 | `synergy_crypto_pump` | ML/R&D раннего обнаружения криптовалютных импульсов/pump-режимов. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 15 | `synergy_market_graph` | Граф рыночных сущностей, зависимостей и отношений. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 16 | `synergy_market_maker` | Market-making: quoting, inventory, risk и микроструктурные контуры. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 17 | `synergy_marketvision` | Perception/feature layer: режимы, структуры и рыночное представление. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 18 | `synergy_midas_ai` | Интегрированный слой market intelligence, моделей и стратегии. | FEDERATION_INTEGRATED | DIRECT_REVIEW | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 19 | `synergy_midas_ai_trading_system` | Большая экспериментальная техническая ветка MIDAS trading system. | EXTERNAL_RUNTIME_PENDING | REGISTRY_BASED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 20 | `synergy_midas_institutional` | Институциональная архитектура data → model → portfolio → risk → execution. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 21 | `synergy_quantlab` | Quant R&D лаборатория, статистические проверки и исследование стратегий. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 22 | `synergy_relative_value` | Relative-value / market-neutral исследования. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 23 | `synergy_riskguard` | Независимый risk/veto слой для торговых и финансовых систем. | FEDERATION_INTEGRATED | DIRECT_REVIEW | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 24 | `synergy_trademux` | Маршрутизация торговых intents/стратегий к исполнимым каналам. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **FLAGSHIP** | Подробный кейс / верхний уровень |

### AI, Agents & Developer Tools

| # | Repository | Что это / какую компетенцию показывает | Maturity | Evidence | Visibility | Tier | Рекомендация |
|---:|---|---|---|---|---|---|---|
| 25 | `synergy_agentic_ai_economy` | Экономика AI-агентов: задачи, контракты, рынки и agent-to-agent workflows. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 26 | `synergy_agi_autopilot` | Планирование, DAG-оркестрация и ограниченное автономное исполнение. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 27 | `synergy_agi_nexus` | Архитектура NEXUS/AGI, reasoning и world-model R&D. | FEDERATION_INTEGRATED | DIRECT_REVIEW | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 28 | `synergy_agi_olga` | Историческая OLGA/AGI линия и исследовательская база поколений NEXUS. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 29 | `synergy_ai_coder` | AI Coder, compiler/build tooling и автоматизация разработки. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 30 | `synergy_ai_company` | Концепция AI-native компании с агентами, процессами и контрактами. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 31 | `synergy_ai_language` | Repository-aware coding agent и семантическая трассируемость требований/изменений. | FEDERATION_INTEGRATED | DIRECT_REVIEW | public | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 32 | `synergy_gllm_nexus` | GLLM/NEXUS research line, бенчмарки и OOS-протоколы. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 33 | `synergy_nexus_science_agent` | Научный агент: поиск, гипотезы, evidence и оркестрация исследований. | FEDERATION_INTEGRATED | DIRECT_REVIEW | private | **FLAGSHIP** | Подробный кейс / верхний уровень |

### Finance & Real Economy

| # | Repository | Что это / какую компетенцию показывает | Maturity | Evidence | Visibility | Tier | Рекомендация |
|---:|---|---|---|---|---|---|---|
| 34 | `synergy_ai_financial_system` | AI/R&D для управления финансовыми моделями, капиталом и экономическими контурами. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 35 | `synergy_cashero` | Эксперименты с денежными потоками, платежными сценариями и финансовой автоматизацией. | SECURITY_BLOCKED | DOC_VERIFIED | private | **HOLD** | Не продвигать до устранения security issue |
| 36 | `synergy_eurasian` | Модели реальной экономики, индустрии и долгосрочной экономической архитектуры. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 37 | `synergy_financial_os` | Канонический слой учета, NAV, обязательств, ликвидности и финансового риска. | FEDERATION_INTEGRATED | DIRECT_REVIEW | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 38 | `synergy_matrix_sota` | Документация debt/credit lifecycle, maturity и требований к учету капитала. | DOCUMENTATION_ONLY | DIRECT_REVIEW | public | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 39 | `synergy_pay_system` | Платежные маршруты, settlement/reconciliation и платежная инфраструктура. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |

### Blockchain & Monetary

| # | Repository | Что это / какую компетенцию показывает | Maturity | Evidence | Visibility | Tier | Рекомендация |
|---:|---|---|---|---|---|---|---|
| 40 | `print_money_synergychain` | R&D программируемой эмиссии, ликвидности, mint/burn и внешнего обеспечения. | DOCUMENTATION_ONLY | DOC_VERIFIED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 41 | `synergy_2chain_qe` | Двухцепочечные модели QE, арбитража и ликвидности в DeFi/fork-среде. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 42 | `synergy_ai_blockchain` | Блокчейн- и trust-layer с PQ/EVM-направлением и проверяемыми состояниями. | FEDERATION_INTEGRATED | DIRECT_REVIEW | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 43 | `synergy_blochain_budget` | Трассируемость бюджетов и provenance финансовых потоков на блокчейне. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 44 | `synergy_chain` | Экспериментальная chain/token/economic ветка SINERGYCHAIN. | NEEDS_HARDENING | DOC_VERIFIED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 45 | `synergy_chain_print_money` | Концептуальная связка chain-механики с monetary/emission R&D. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 46 | `synergy_graph_print_money` | Графовый Economic OS и моделирование денежных/эмиссионных контуров. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 47 | `synergy_metachain` | Cross-chain/bridge логика lock/burn → mint/claim и защита от повторного исполнения. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 48 | `synergy_qe` | Концептуальный QE Engine. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 49 | `synergy_usds` | Экспериментальная USDS/stablecoin и Base-fork экономика. | SECURITY_BLOCKED | REGISTRY_BASED | private | **HOLD** | Не продвигать до устранения security issue |

### Infrastructure, Compute & Security

| # | Repository | Что это / какую компетенцию показывает | Maturity | Evidence | Visibility | Tier | Рекомендация |
|---:|---|---|---|---|---|---|---|
| 50 | `dlp_solver` | Криптографический R&D Reverse-EXP/DLP с воспроизводимыми экспериментами и ресурсными оценками. | FEDERATION_INTEGRATED | DIRECT_REVIEW | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 51 | `synegy_ai_compress` | R&D компрессии AI-данных/моделей и архивного субстрата. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 52 | `synergy_gguf_compress` | Исследования компрессии GGUF/LLM-моделей. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 53 | `synergy_motherboard_xpu_xml` | Экспериментальное описание XPU/EML и вычислительной платформы. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 54 | `synergy_net` | P2P/mesh transport и data-plane между узлами. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 55 | `synergy_post_quantum_radio` | Концепция post-quantum защищенного физического/радио транспорта. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 56 | `synergy_qr_compress` | Temporal dictionary / QR compression и повторное использование структуры данных. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **STRONG** | Полная карточка в Engineering Atlas |
| 57 | `synergy_shhts` | Экспериментальный security/transport placeholder. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 58 | `synergy_shttps` | Экспериментальный secure-transport/HTTPS-like слой. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 59 | `synergy_turbo_linux` | Host/OS слой: изоляция, сервисы и runtime узла. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **HOLD** | Не продвигать до устранения security issue |

### Science & Mathematical R&D

| # | Repository | Что это / какую компетенцию показывает | Maturity | Evidence | Visibility | Tier | Рекомендация |
|---:|---|---|---|---|---|---|---|
| 60 | `binary_quantum_theory` | Binary Quantum Gravity: конечные операторы, численные сертификаты и proof gates. | FEDERATION_INTEGRATED | DIRECT_REVIEW | public | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 61 | `epstein_network` | Исследовательский knowledge/provenance graph источников и связей. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **HOLD** | Не выносить в HR-верхний уровень |
| 62 | `synergy_cold_nuclear` | Вычислительные эксперименты для низкоэнергетических ядерных гипотез. | FEDERATION_INTEGRATED | REGISTRY_BASED | public | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 63 | `synergy_complex_matrix_multiplication` | Структурированные матричные операторы, FFT/Q-CNO, Transformer compression и kernel benchmarks. | ACTIVE_EXPERIMENTAL / direct audit | DIRECT_REVIEW | public | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 64 | `synergy_computing_topology` | Экспериментальный computing stack: compact descriptors/indexes, LLVM/Linux, correctness-first benchmarks. | V4_VALIDATED_R&D / direct audit | DIRECT_REVIEW | private | **FLAGSHIP** | Подробный кейс / верхний уровень |

### Architecture & Governance

| # | Repository | Что это / какую компетенцию показывает | Maturity | Evidence | Visibility | Tier | Рекомендация |
|---:|---|---|---|---|---|---|---|
| 65 | `synergy_apps` | Master-реестр приложений и их связей. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 66 | `synergy_megaproject` | Knowledge graph мегапроектов, frontier technologies, институтов и источников. | FEDERATION_INTEGRATED | DIRECT_REVIEW | public | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 67 | `synergy_meta_os` | Runtime-оркестратор полного узла и межсервисных контуров. | FEDERATION_INTEGRATED | DIRECT_REVIEW | private | **FLAGSHIP** | Подробный кейс / верхний уровень |
| 68 | `synergy_project` | Экономический и продуктовый master dossier. | FEDERATION_INTEGRATED | REGISTRY_BASED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 69 | `synergy_system` | Архитектурный/governance корень федерации репозиториев. | GOVERNANCE_ROOT | REGISTRY_BASED | private | **SUPPORTING** | Краткая карточка / часть семейства |

### Apps & Interfaces

| # | Repository | Что это / какую компетенцию показывает | Maturity | Evidence | Visibility | Tier | Рекомендация |
|---:|---|---|---|---|---|---|---|
| 70 | `shtenco.github.io` | Публичное портфолио и навигационная витрина проектов. | NON_RUNTIME_SURFACE | DOC_VERIFIED | public | **SURFACE** | Использовать как интерфейс/витрину, не как core engineering |
| 71 | `shtencoauantai.github.io` | Публичный Quant/AI web-портал для отдельных направлений. | NON_RUNTIME_SURFACE | DOC_VERIFIED | public | **SURFACE** | Использовать как интерфейс/витрину, не как core engineering |
| 72 | `sinergy_app` | Приложенческий shell и ранняя продуктовая концепция SINERGY. | DOCUMENTATION_ONLY | DOC_VERIFIED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 73 | `sinergy_super_app` | Super-app оболочка для объединения пользовательских сервисов. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 74 | `synergy_app` | Пользовательский финансовый интерфейс и клиентский слой. | FEDERATION_INTEGRATED | DOC_VERIFIED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 75 | `synergy_app_family` | Концепция семейства пользовательских приложений. | DOCUMENTATION_ONLY | REGISTRY_BASED | private | **CONCEPT** | Только как R&D/концепт, без production-claims |
| 76 | `synergy_messenger` | Коммуникационный клиент и мессенджер экосистемы. | NEEDS_HARDENING | REGISTRY_BASED | private | **SUPPORTING** | Краткая карточка / часть семейства |
| 77 | `synergychain.github.io` | Публичная web-витрина SINERGYCHAIN. | NON_RUNTIME_SURFACE | DOC_VERIFIED | public | **SURFACE** | Использовать как интерфейс/витрину, не как core engineering |

### Недостающие позиции из целевых 79

| # | Repository | Status |
|---:|---|---|
| 78 | — | NOT VISIBLE TO CONNECTOR — название и содержимое не установлены |
| 79 | — | NOT VISIBLE TO CONNECTOR — название и содержимое не установлены |

## Правила публичного портфолио

1. Главная страница: 10–15 наиболее понятных flagship-кейсов.
2. Engineering Atlas: все 77 доступных репозиториев, сгруппированные по 8 доменам.
3. Private repositories описываются по проверенной роли и evidence, без ссылки на недоступный исходный код как будто он публичный.
4. Backtest/benchmark не называется production performance. Локальный GREEN не называется внешним аудитом.
5. Documentation-only/placeholder проекты не описываются словами «готовая система».
6. Security-blocked проекты не используются для демонстрации deployment readiness.
