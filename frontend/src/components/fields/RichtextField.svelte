<script>
import { createEventDispatcher } from "svelte";
export let key;
export let record;
export let field_options;

let is_editing = false;
let new_val = record[key];
let dispatch = createEventDispatcher();
function handle_edit_click() {
  if (field_options.editable) {
    is_editing = true;
  }
}

function handle_input(event) {
  // if enter key pressed or input loses focus then stop editing
  if (event.key === "Enter" || event.type === "blur") {
    is_editing = false;
  }
  if (event.key === "Escape") {
    is_editing = false;
    new_val = record[key];
  }

  //   if the input is diffrent, then update the record and send a signal to the parent
  if (new_val !== record[key] && is_editing === false) {
    record[key] = new_val;
    dispatch("cell_updated", { key, value: new_val, record: record });
  }
}
</script>

<td on:click={handle_edit_click}>
  <div class="number-field">
    {#if is_editing}
      <textarea bind:value={new_val} on:keypress={handle_input} on:blur={handle_input} autofocus />
    {:else}
      {record[key] || "ריק"}
    {/if}
  </div>
</td>

<style lang="scss">
.number-field {
  input {
    width: 100%;
    // max-width: 70px;
  }
}
</style>
