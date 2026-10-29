# Franka Panda MuJoCo Demo

Small MuJoCo simulation scripts for a Franka Emika Panda arm.

## Setup

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install mujoco numpy imageio imageio-ffmpeg
```

The robot model is provided by the `mujoco_menagerie` submodule:

```powershell
git submodule update --init --recursive
```

## Run

Launch the interactive simulation:

```powershell
python arm.py
```

Render a 10-second episode and save `arm.mp4` plus `episode_log.csv`:

```powershell
python record.py
```