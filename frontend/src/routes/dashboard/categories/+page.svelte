<script>
import { onMount } from "svelte";
import { CategoriesDataFetcher } from "../../../network/DataFetcher";
import DataTable from "../../../components/table_panels/DataTable.svelte";
import { page } from "$app/stores";
import * as Types from "./../../../lib/types.js";

// import { layoutPrefereces } from "../../stores/layoutPrefereces";

let error = undefined;

/**
 * @type {DataFetcher}
 */
let dataFetcher;

/**
 * @type {any[]}
 */
let data;

let sizes_options;

/**
 * @type {Types.FieldsOption[]}
 */
let fields_options;
onMount(async () => {
  fields_options = [
    {
      key: "id",
      type: "number",
      editable: false,
      label: "מזהה",
    },
    {
      key: "name",
      type: "text",
      editable: true,
      label: "שם",
    },
  ];
  dataFetcher = new CategoriesDataFetcher();
  await get_data();
});

async function get_data() {
  console.log("get_data");
  let params = $page.url.searchParams;
  try {
    data = await dataFetcher.getData(params);
  } catch (_error) {
    error = _error;
  }
}

function handle_cell_updated(event) {
  let { key, value, record } = event.detail;
  let record_id = record["id"];
  dataFetcher.update_record(record_id, record);
}
</script>

{#if error !== undefined}
  <div class="alert alert-danger" role="alert">
    {error.message}
    <button
      class="btn btn-primary"
      on:click={() => {
        location.reload();
      }}>רענן</button
    >
  </div>
  <!-- refresh the page button -->
{/if}
<DataTable
  on:cell_updated={handle_cell_updated}
  on:filter_updated={get_data}
  title="קטגוריות"
  {data}
  side_filters={[
    {
      query_param_key: "name",
      type: "text",
      label: "שם",
    },
  ]}
  {fields_options}
/>
