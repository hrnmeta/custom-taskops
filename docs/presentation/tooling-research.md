# Internal tooling research

Checked October 14, 2026. Sources retained for the internal-tooling comparison.

Research checked internal documentation on October 14, 2026. Existing tools already support configuration and orchestration; do not claim that Custom TaskOps uniquely supports customization. Team AAI provides shared maintained procedures; aai-long-horizon /lh-flow already coordinates scaffold, checkpoints, oracle, rollouts, review, coverage, and audit. Lambo Express v1.3.0 is an end-to-end long-horizon SWE pipeline with idea-partner, seeded, resume, and full-auto modes. Harvester V2 converts commits into tasks and includes calibration, per-track prompts, presets, and flags. Task-factory D120600849 is committed (landed September 22, 2026), covers SWE/TBench, and is configured via ~/.task-factory.toml. Custom TaskOps adds a personally maintained orchestration layer and policies reusable across operations/tracks. Integration with a named generator is a composition choice, not a claim that all integrations ship today.

Official skills: https://fb.workplace.com/groups/aaiado/permalink/1498276205349755/
Long-horizon flow: https://fb.workplace.com/groups/1583165033535643/permalink/1615245886994224/
Lambo Express: https://fb.workplace.com/groups/2233341433896796/permalink/1604944231245274/
Harvester V2: https://www.internalfb.com/wiki/AAI_Labs/Data_Generation/Automation/Recipes/Harvester/Harvester_V2/Quick_Start/
Task factory: https://www.internalfb.com/diff/D120600849

Positioning: customization already exists in these tools. Custom TaskOps packages personal instructions, policy, and orchestration as a user-owned layer. It can reuse existing skills and pipelines with explicit handoffs; named integrations are choices, not all implemented connectors.
