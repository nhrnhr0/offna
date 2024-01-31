<script>
import { onMount } from "svelte";
import { SizesDataFetcher, SizesGroupsDataFetcher, OptionsDataStore } from "../../../network/DataFetcher";
import DataTable from "../../../components/table_panels/DataTable.svelte";
import { page } from "$app/stores";
import * as Types from "./../../../lib/types.js";

// import { layoutPrefereces } from "../../stores/layoutPrefereces";

/**
 * @type {SizesDataFetcher}
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
  let size_group_option_fetcher = new OptionsDataStore();
  size_group_option_fetcher.set_fetcher(new SizesGroupsDataFetcher());
  await size_group_option_fetcher.load_options();
  size_group_options = size_group_option_fetcher.get_options();
  console.log("size_group_options", size_group_options);
  fields_options = [
    {
      key: "id",
      type: "number",
      editable: false,
      sortable: true,
      filterable: true,
      label: "מזהה",
    },

    {
      key: "size",
      type: "text",
      editable: true,
      sortable: true,
      filterable: true,
      label: "שם",
    },
    {
      key: "order",
      type: "number",
      editable: true,
      sortable: true,
      filterable: true,
      label: "סדר",
    },
    {
      key: "size_group",
      type: "select",
      editable: true,
      sortable: true,
      filterable: true,
      label: "קבוצה",
      options: size_group_options,
    },
  ];
  dataFetcher = new SizesDataFetcher();
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
  title="מידות"
  {data}
  side_filters={[
    {
      query_param_key: "group",
      type: "multiselect",
      // options_fetcher: size_group_option_fetcher,
      options: size_group_options,
      label: "קבוצה",
    },
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
