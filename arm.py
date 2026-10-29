import time
import numpy as np
import mujoco
import mujoco.viewer

model = mujoco.MjModel.from_xml_path(
    "mujoco_menagerie/franka_emika_panda/scene.xml"
)
data = mujoco.MjData(model)

print("joints:", model.njnt, "actuators:", model.nu)

# Start from the arm's built-in "home" pose if the model defines one
if model.nkey > 0:
    mujoco.mj_resetDataKeyframe(model, data, 0)
home_ctrl = data.ctrl.copy()

with mujoco.viewer.launch_passive(model, data) as viewer:
    start = time.time()
    while viewer.is_running() and time.time() - start < 30:
        t = time.time() - start
        data.ctrl[:] = home_ctrl
        data.ctrl[0] = home_ctrl[0] + 0.5 * np.sin(t)  # swing the base joint
        mujoco.mj_step(model, data)
        viewer.sync()
        time.sleep(model.opt.timestep)