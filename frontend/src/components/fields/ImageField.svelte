<script>
import { createEventDispatcher } from "svelte";
const BACKEND_URL = "http://127.0.0.1:8000";
export let key;
export let record;
export let field_options;
let file = undefined;
let is_editing = false;

let new_val = record[key];
let preview_url = "";
let dispatch = createEventDispatcher();

function handle_edit_click() {
  if (field_options.editable) {
    is_editing = true;
  }
}

function handle_abort(e) {
  e.stopPropagation();
  is_editing = false;
  new_val = record[key];
}

function handle_save(e) {
  e.stopPropagation();
  is_editing = false;
  record[key] = file;
  debugger;

  dispatch("cell_updated", { key, value: file, record: record });
}
</script>

<td on:click={handle_edit_click}>
  {#if is_editing}
    <img src={preview_url} alt="" width="50px" max-height="50px" />
    <input
      type="file"
      bind:value={new_val}
      on:change={(e) => {
        file = e.target.files[0];
        preview_url = URL.createObjectURL(file);
      }}
    />
    <!-- image preview -->
    <div class="mrow">
      <button class="btn btn-success" on:click={handle_save}>✓</button>
      <button class="btn btn-danger" on:click={handle_abort}>✗</button>
    </div>
  {:else if record[key]}
    <img src={BACKEND_URL + record[key]} alt="" width="50px" max-height="50px" />
  {:else}1
    <div class="error">No image</div>
  {/if}
</td>
