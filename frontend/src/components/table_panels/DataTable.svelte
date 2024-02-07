<script>
import * as Types from "./../../lib/types.js";

import { onMount } from "svelte";
import { DataFetcher, OptionsDataStore } from "../../network/DataFetcher";
import NumberField from "../fields/NumberField.svelte";
import TextField from "../fields/TextField.svelte";
import SelectField from "../fields/SelectField.svelte";
import { createEventDispatcher } from "svelte";
import TableSideFilters from "./TableSideFilters.svelte";
import { browser } from "$app/environment";
import MultiSelectField from "../fields/MultiSelectField.svelte";
import ColorField from "../fields/ColorField.svelte";
import RichtextField from "../fields/RichtextField.svelte";
import ImageField from "../fields/ImageField.svelte";
import DatePlusDateBeforeField from "../fields/DatePlusDateBeforeField.svelte";

/**
 * @type {any[]}
 */
export let data;

/**
 * @type {string}
 */
export let title;
/**
 * @type {Types.FieldsOption[] | undefined}
 */
export let fields_options;

export let side_filters;
/**
 * @type {writable<Types.FieldsOption[]> | undefined}
 */
export let display_fields_options;

let dispatch = createEventDispatcher();

onMount;

function handle_cell_updated(event) {
  let { key, value, record } = event.detail;
  dispatch("cell_updated", { key, value: value, record: record });
}
function filter_updated() {
  dispatch("filter_updated");
}
function order_updated() {
  dispatch("order_updated");
}
</script>

<div class="data-table">
  <!-- Your table content goes here -->
  <div class="">
    <h2 class="title">{title}</h2>
    <!-- ordering  options -->
    <div class="panel">
      <table class="table table-striped table-hover my-table">
        {#if fields_options === undefined}
          <thead>
            <tr>
              <th> </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td></td>
            </tr>
          </tbody>
        {:else if display_fields_options.length === 0}
          <p>fields_options is empty</p>
        {:else}
          <thead>
            <tr>
              {#each display_fields_options as field}
                <th>
                  {field.label}
                </th>
              {/each}
            </tr>
          </thead>
          <tbody>
            {#if data}
              {#each data as row, i}
                <tr>
                  {#each display_fields_options as field}
                    <!-- <td> {JSON.stringify(field.type)} </td> -->
                    {#if field.type === "number"}
                      <NumberField key={field.key} record={row} field_options={field} on:cell_updated={handle_cell_updated}></NumberField>
                    {:else if field.type === "text"}
                      <TextField key={field.key} record={row} field_options={field} on:cell_updated={handle_cell_updated}></TextField>
                    {:else if field.type === "select"}
                      <SelectField key={field.key} record={row} field_options={field} on:cell_updated={handle_cell_updated}></SelectField>
                    {:else if field.type === "multi_select"}
                      <MultiSelectField key={field.key} record={row} field_options={field} on:cell_updated={handle_cell_updated}></MultiSelectField>
                    {:else if field.type == "color"}
                      <ColorField key={field.key} record={row} field_options={field} on:cell_updated={handle_cell_updated}></ColorField>
                    {:else if field.type == "richtext"}
                      <RichtextField key={field.key} record={row} field_options={field} on:cell_updated={handle_cell_updated}></RichtextField>
                    {:else if field.type == "image"}
                      <ImageField key={field.key} record={row} field_options={field} on:cell_updated={handle_cell_updated}></ImageField>
                    {:else if field.type == "date_plus_datebefore"}
                      <DatePlusDateBeforeField key={field.key} record={row} field_options={field} on:cell_updated={handle_cell_updated}></DatePlusDateBeforeField>
                    {:else}
                      <td>-</td>
                    {/if}
                  {/each}
                </tr>
              {/each}
            {/if}
          </tbody>
        {/if}
      </table>
      <TableSideFilters on:filter_updated={filter_updated} {side_filters} {fields_options} bind:display_fields_options></TableSideFilters>
    </div>
  </div>
</div>

<style lang="scss">
.data-table {
  height: 100vh;
  overflow-y: auto;
  border: 1px solid black;
  // border: 1px solid black;
  .panel {
    display: grid;
    grid-template-columns: 8fr 2fr;
    grid-gap: 1rem;
  }
  .my-table {
    // table-layout: fixed;
    width: 100%;
    :global(td),
    :global(th) {
      text-align: center;
      box-sizing: border-box;
    }
  }
  .title {
    text-align: center;
  }
}

// if the table has too few elements, the cells height will be too big
// this will fix it
.table {
  tbody {
    tr {
      :global(td) {
        // padding-top: 0.25rem;
        // padding-bottom: 0.25rem;
      }
    }
  }
}
</style>
