<script>
import DashBoardNav from "../../components/DashboardNav.svelte";
import { SvelteToast } from "@zerodevx/svelte-toast";
let svelte_toast_options = {
  duration: 4000,
  type: "success",
  pausable: true,
  dismissable: true,
};
</script>

<SvelteToast options={svelte_toast_options} />

<div class="dashboard">
  <DashBoardNav />
  <div class="dashboard-content">
    <slot />
  </div>
</div>

<style lang="scss">
.dashboard {
  display: flex;
  height: 100%;
  .dashboard-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
}
</style>
