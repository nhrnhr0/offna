<script>
import * as Types from "./../../lib/types.js";
import { onMount } from "svelte";
import { MultiSelect } from "svelte-multiselect";
import { createEventDispatcher } from "svelte";
/**
 * @type {string}
 */
export let key;
/**
 * @type {Object}
 */
export let record;
export let field_options;
let is_editing = false;
let dispatch = createEventDispatcher();

/**
 * @type {{id: number, label: string}[]}
 */
let optinos = field_options.options;
/**
 * @type {number[] | undefined}
 */
let new_value = optinos.filter((option) => record[key].includes(option.id));

function handle_save(e) {
  e.stopPropagation();
  is_editing = false;
  record[key] = new_value.map((value) => value.id);
  dispatch("cell_updated", { key, value: new_value, record: record });
}

function handle_abort(e) {
  e.stopPropagation();
  is_editing = false;
  new_value = optinos.filter((option) => record[key].includes(option.id));
}
</script>

<td on:click={() => (is_editing = true)}>
  {#if is_editing}
    <div class="mrow">
      <MultiSelect bind:selected={new_value} options={optinos}></MultiSelect>
      <button class="btn btn-success" on:click={handle_save}>✓</button>
      <button class="btn btn-danger" on:click={handle_abort}>✗</button>
    </div>
  {:else}
    {new_value?.map((value) => value.label).join(", ")}
  {/if}
</td>

<style lang="scss">
.mrow {
  display: flex;
  align-items: center;
}
</style>
