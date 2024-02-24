<script>
import { createEventDispatcher, onMount } from "svelte";
import IconEdit from "../Icons/IconEdit.svelte";
import IconDelete from "../Icons/IconDelete.svelte";
export let key;
export let record;
export let field_options;
let id = record[key];

let dispatch = createEventDispatcher();
</script>

<td>
  <div class="actions-wraper">
    {#each field_options.options as action}
      {#if action.type == "edit"}
        <a href={action.path.replace("{id}", id)} class="btn btn-primary" title={action.label}> <IconEdit /></a>
      {:else if action.type == "delete"}
        <a href={action.path.replace("{id}", id)} class="btn btn-danger" title={action.label}> <IconDelete /></a>
      {/if}
    {/each}
  </div>
</td>

<style lang="scss">
.actions-wraper {
  width: fit-content;
  display: flex;
  justify-content: space-between;
  a {
    margin: 0 5px;
  }
}
</style>
