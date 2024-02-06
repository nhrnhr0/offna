<script>
import { onMount } from "svelte";
import { CategoriesDataFetcher, ColorsDataFetcher, OptionsDataStore, ProductsDataFetcher, SizesDataFetcher, SizesGroupsDataFetcher } from "../../../network/DataFetcher";
import DataTable from "../../../components/table_panels/DataTable.svelte";
import { page } from "$app/stores";
import * as Types from "./../../../lib/types.js";
import { toast } from "@zerodevx/svelte-toast";

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
      type: "date_plus_datebefore",
      editable: false,
      label: "נוצר",
    },
    {
      key: "updated_at",
      type: "date_plus_datebefore",
      editable: false,
      label: "עודכן",
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
  let data_to_send = { id: record_id, [key]: value };
  dataFetcher
    .update_record(record_id, data_to_send)
    .then((res) => {
      let msg = (fields_options.find((f) => f.key === key)?.label || key) + " עודכן בהצלחה";
      toast.push(msg);

      // find and replace the updated record
      let index = data.findIndex((r) => r.id === record_id);
      data[index] = res;
    })
    .catch((err) => {
      console.error("record update failed", err);
      toast.push("עדכון נכשל", {
        theme: {
          "--toastColor": "red",
          "--toastBackground": "black",
        },
      });
    });
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
