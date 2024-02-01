<script>
import { onMount } from "svelte";
import { SizesDataFetcher, SizesGroupsDataFetcher, OptionsDataStore } from "../../../network/DataFetcher";
import DataTable from "../../../components/table_panels/DataTable.svelte";
import { page } from "$app/stores";
import * as Types from "./../../../lib/types.js";

// import { layoutPrefereces } from "../../stores/layoutPrefereces";

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
  let sizes_options_fetcher = new OptionsDataStore();
  sizes_options_fetcher.set_fetcher(new SizesDataFetcher());
  await sizes_options_fetcher.load_options();
  sizes_options = sizes_options_fetcher.get_options();
  console.log("size_group_options", sizes_options);
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
      key: "name",
      type: "text",
      editable: true,
      sortable: true,
      filterable: true,
      label: "שם",
    },
    {
      key: "sizes_ids",
      type: "multi_select",
      editable: true,
      sortable: true,
      filterable: true,
      label: "מידות",
      options: sizes_options,
    },
  ];
  dataFetcher = new SizesGroupsDataFetcher();
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
      query_param_key: "name",
      type: "text",
      label: "שם",
    },
  ]}
  {fields_options}
/>
