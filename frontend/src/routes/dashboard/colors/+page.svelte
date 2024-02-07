<script>
import { onMount } from "svelte";
import { ColorsDataFetcher } from "../../../network/DataFetcher";
import DataTable from "../../../components/table_panels/DataTable.svelte";
import { page } from "$app/stores";
import * as Types from "./../../../lib/types.js";
import { userPreferenceColorsTable } from "../../../stores/UserPreference";
// import { layoutPrefereces } from "../../stores/layoutPrefereces";

/**
 * @type {ColorsDataFetcher}
 */
let dataFetcher;

/**
 * @type {any[]}
 */
let data;

let size_group_options;

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
    {
      key: "color",
      type: "color",
      editable: true,
      label: "צבע",
    },
    {
      key: "order",
      type: "number",
      editable: true,
      label: "סדר",
    },
  ];
  dataFetcher = new ColorsDataFetcher();
  await get_data();
});

async function get_data() {
  console.log("get_data");
  let params = $page.url.searchParams;
  data = await dataFetcher.getData(params);
}

function handle_cell_updated(event) {
  let { key, value, record } = event.detail;
  let record_id = record["id"];
  debugger;
  dataFetcher.update_record(record_id, record);
}
</script>

<DataTable
  on:cell_updated={handle_cell_updated}
  on:filter_updated={get_data}
  bind:display_fields_options={$userPreferenceColorsTable}
  title="צבעים"
  {data}
  side_filters={[
    {
      query_param_key: "name",
      type: "text",
      label: "שם",
    },
    {
      query_param_key: "order",
      type: "number",
      label: "סדר",
    },
  ]}
  {fields_options}
/>

<!-- display_fields={["id", "size", "order", "size_group"]} -->
