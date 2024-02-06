<script>
import { onMount } from "svelte";
import { OptionsDataStore } from "../../network/DataFetcher";
import { createEventDispatcher } from "svelte";
let dispatch = createEventDispatcher();

export let key;
export let record;
export let field_options;
let new_val = record[key];
let is_editing = false;

function handle_edit_click() {
  if (field_options.editable) {
    is_editing = true;
  }
}

function handle_save(e) {
  e.stopPropagation();
  debugger;
  is_editing = false;
  record[key] = new_val;
  dispatch("cell_updated", { key, value: new_val, record: record });
}

function handle_abort(e) {
  e.stopPropagation();
  is_editing = false;
  new_val = record[key];
}
</script>

<td on:click={handle_edit_click}>
  {#if field_options.options !== undefined}
    <div class="text-field">
      {#if is_editing}
        <div style="display: flex; align-items: center;">
          <select bind:value={new_val} class="form-select">
            {#each field_options.options as option}
              <option value={option.id}>{option.label}</option>
            {/each}
          </select>
          <!-- approve  / reject -->
          <button class="btn btn-success" on:click={handle_save}>✓</button>
          <button class="btn btn-danger" on:click={handle_abort}>✗</button>
        </div>
      {:else if field_options && field_options.options && field_options.options.length > 0}
        {field_options.options.find((option) => option.id === record[key])?.label ?? "ריק"}
      {/if}
    </div>
  {:else}
    <div class="error">No options fetcher provided</div>
  {/if}
</td>
