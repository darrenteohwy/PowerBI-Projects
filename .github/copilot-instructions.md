# Copilot Instructions for PowerBI-Projects

## Overview
This repository contains PowerBI-related projects, with a focus on data analysis and visualization. The main project currently is the "Spotify 2023 Project".

## Architecture & Data Flow
- **Data Source:** The primary dataset is `spotify-2023.csv` located in `Spotify 2023 Project/`.
- **Analysis Scripts:** Python scripts (e.g., `spotifyapi.py`) are used for data processing, analysis, and possibly API integration.
- **Images:** Visualizations and outputs are stored in the `images/` subdirectory.

## Developer Workflows
- **No build system or test framework is present.**
- **Run analysis scripts directly:**
  - Example: `python "Spotify 2023 Project/spotifyapi.py"`
- **Data updates:** Place new CSVs in the project folder and update scripts to reference them.
- **Visualization outputs:** Save generated images to `images/` for organization.

## Project-Specific Conventions
- All code and data for a project are grouped under a single folder (e.g., `Spotify 2023 Project/`).
- Scripts are expected to be run manually; there are no automation or CI/CD pipelines.
- Use clear, descriptive filenames for datasets and images.
- Keep analysis logic in Python scripts; avoid mixing with visualization assets.

## Integration Points
- External dependencies (e.g., pandas, matplotlib) may be required for analysis scripts. Install as needed with `pip install`.
- No explicit API keys or secrets are present; if needed, document usage in the script header.

## Examples
- To process Spotify data: Edit and run `spotifyapi.py`.
- To add a new analysis: Create a new script in the project folder and document its purpose at the top.

## Key Files & Directories
- `Spotify 2023 Project/spotify-2023.csv`: Main dataset
- `Spotify 2023 Project/spotifyapi.py`: Main analysis script
- `Spotify 2023 Project/images/`: Output visualizations

## Guidance for AI Agents
- Focus on data analysis, transformation, and visualization tasks.
- Maintain separation between code, data, and output assets.
- Document any new scripts or workflows in the project folder.
- If adding new dependencies, note them in the script header.
