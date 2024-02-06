<script>
import { page } from "$app/stores";
export let filter;
let query_param_key = filter.query_param_key;

let query_param_value_lte = get_value_from_query_param(query_param_key + "__lte");
let query_param_value_gte = get_value_from_query_param(query_param_key + "__gte");

function get_value_from_query_param(key) {
  return $page.url.searchParams.get(key);
}

function set_gte_date(date) {
  return function (event) {
    event.preventDefault();
    query_param_value_gte = str_to_date(date);
    handle_input_change();
  };
}
function set_lte_date(date) {
  return function (event) {
    event.preventDefault();
    query_param_value_lte = str_to_date(date);
    handle_input_change();
  };
}
function str_to_date(str) {
  if (str == "today") {
    return new Date().toISOString().split("T")[0];
  } else if (str == "yesterday") {
    let d = new Date();
    d.setDate(d.getDate() - 1);
    return d.toISOString().split("T")[0];
  } else if (str == "last_week") {
    let d = new Date();
    d.setDate(d.getDate() - 7);
    return d.toISOString().split("T")[0];
  }
  return "";
}

function handle_input_change() {
  $page.url.searchParams.delete(query_param_key + "__gte");
  $page.url.searchParams.delete(query_param_key + "__lte");
  if (query_param_value_gte) {
    $page.url.searchParams.set(query_param_key + "__gte", query_param_value_gte);
  }
  if (query_param_value_lte) {
    $page.url.searchParams.set(query_param_key + "__lte", query_param_value_lte);
  }
}
</script>

<!-- from and to date fields -->
<div class="form-group">
  <div class="row">
    <div class="col">
      <label for="from_date">מתאריך</label>
      <input type="date" bind:value={query_param_value_gte} class="form-control" on:change={handle_input_change} />
      <a href="#" on:click={set_gte_date("today")}>היום</a>, <a href="#" on:click={set_gte_date("yesterday")}>אתמול</a>,
      <a href="#" on:click={set_gte_date("last_week")}>שבוע אחרון</a>
    </div>
  </div>
  <div class="row">
    <div class="col">
      <label for="to_date">עד תאריך</label>
      <input type="date" bind:value={query_param_value_lte} class="form-control" on:change={handle_input_change} />
      <a href="#" on:click={set_lte_date("today")}>היום</a>, <a href="#" on:click={set_lte_date("yesterday")}>אתמול</a>,
      <a href="#" on:click={set_lte_date("last_week")}>שבוע אחרון</a>
    </div>
  </div>
</div>
