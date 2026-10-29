import csv
import numpy as np
import mujoco
import imageio

model = mujoco.MjModel.from_xml_path("mujoco_menagerie/franka_emika_panda/scene.xml")
data = mujoco.MjData(model)

if model.nkey > 0:
    mujoco.mj_resetDataKeyframe(model, data, 0)
home_ctrl = data.ctrl.copy()

fps = 30
duration = 10  # seconds of simulated time
renderer = mujoco.Renderer(model, 480, 640)
frames = []

with open("episode_log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time"] + [f"q{i}" for i in range(7)] + ["ctrl0"])

    while data.time < duration:
        data.ctrl[:] = home_ctrl
        data.ctrl[0] = home_ctrl[0] + 0.5 * np.sin(data.time)
        mujoco.mj_step(model, data)

        # save a frame and a log row at the video frame rate
        if len(frames) < data.time * fps:
            renderer.update_scene(data)
            frames.append(renderer.render())
            writer.writerow([round(data.time, 4)] + list(np.round(data.qpos[:7], 5)) + [round(data.ctrl[0], 5)])

imageio.mimsave("arm.mp4", frames, fps=fps)
print("saved arm.mp4 and episode_log.csv,", len(frames), "frames")