<script>
import { onMount } from "svelte";
import { CategoriesDataFetcher, ColorsDataFetcher, OptionsDataStore, ProductsDataFetcher, SizesDataFetcher, SizesGroupsDataFetcher } from "../../../network/DataFetcher";
import DataTable from "../../../components/table_panels/DataTable.svelte";
import { page } from "$app/stores";
import * as Types from "./../../../lib/types.js";

// import { layoutPrefereces } from "../../stores/layoutPrefereces";

/**
 * @type {any}
 */
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
let colors_options;
let category_options;
let size_group_options;
/**
 * @type {Types.FieldsOption[]}
 */
let fields_options;
onMount(async () => {
  //id,name,sizes,colors,category,price,description,header_image,gallery,size_group,created_at,updated_at
  let res = await Promise.all([
    new OptionsDataStore("id", "size").set_fetcher(new SizesDataFetcher()).load_options(),
    new OptionsDataStore("id", "name").set_fetcher(new ColorsDataFetcher()).load_options(),
    new OptionsDataStore("id", "name").set_fetcher(new CategoriesDataFetcher()).load_options(),
    new OptionsDataStore("id", "name").set_fetcher(new SizesGroupsDataFetcher()).load_options(),
  ]);
  sizes_options = res[0].get_options();
  colors_options = res[1].get_options();
  category_options = res[2].get_options();
  size_group_options = res[3].get_options();
  debugger;
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
      key: "sizes",
      type: "multi_select",
      editable: true,
      label: "מידות",
      options: sizes_options,
    },
    {
      key: "colors",
      type: "multi_select",
      editable: true,
      label: "צבעים",
      options: colors_options,
    },
    {
      key: "category",
      type: "select",
      editable: true,
      label: "קטגוריה",
      options: category_options,
    },
    {
      key: "size_group",
      type: "select",
      editable: true,
      label: "קבוצת מידות",
      options: size_group_options,
    },
    {
      key: "price",
      type: "number",
      editable: true,
      label: "מחיר",
    },
    {
      key: "description",
      type: "richtext",
      editable: true,
      label: "תיאור",
    },
    {
      key: "header_image",
      type: "image",
      editable: true,
      label: "תמונה ראשית",
    },
    {
      key: "gallery",
      type: "image_gallery",
      editable: true,
      label: "גלריה",
    },
    {
      key: "created_at",
      type: "date",
      editable: false,
      label: "נוצר בתאריך",
    },
    {
      key: "updated_at",
      type: "date",
      editable: false,
      label: "עודכן בתאריך",
    },
  ];
  dataFetcher = new ProductsDataFetcher();
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

/**
 * @param event {CustomEvent}
 */
function handle_cell_updated(event) {
  let { key, value, record } = event.detail;
  let record_id = record["id"];
  debugger;
  if (key === "header_image") {
    // record[key] = value;
    dataFetcher.update_image(record_id, value, key).then(() => {
      debugger;
      dataFetcher.update_record(record_id, record);
    });
  } else {
    dataFetcher.update_record(record_id, record);
  }

  // dataFetcher.update_record(record_id, record);
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
  title="מוצרים"
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
