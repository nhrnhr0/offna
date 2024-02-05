<script>
import { createEventDispatcher, onMount } from "svelte";
export let key;
export let record;
export let field_options;
let new_val = record[key];
let is_editing = false;

let dispatch = createEventDispatcher();
</script>

<td
  on:click={() => {
    if (is_editing === false) {
      new_val = record[key];
      is_editing = true;
      setTimeout(() => {
        const colorInput = document.querySelector('input[type="color"]');
        if (colorInput !== null) {
          colorInput.click();
        }
      }, 0);
    }
  }}
>
  <div class="color-field">
    {#if is_editing}
      <input type="color" bind:value={new_val} />
      <button
        class="btn btn-success"
        on:click={(e) => {
          e.preventDefault();
          e.stopPropagation();
          is_editing = false;
          record[key] = new_val;
          dispatch("cell_updated", { key, value: new_val, record: record });
        }}>✓</button
      >
      <button
        class="btn btn-danger"
        on:click={(e) => {
          e.preventDefault();
          e.stopPropagation();
          is_editing = false;
          new_val = record[key];
        }}>✗</button
      >
    {:else}
      <div class="color-box" style="background-color: {record[key]}"></div>
    {/if}
  </div>
</td>

<style lang="scss">
.color-field {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 5px;
  .color-box {
    width: 20px;
    height: 20px;
    border: 1px solid black;
  }
}
</style>
