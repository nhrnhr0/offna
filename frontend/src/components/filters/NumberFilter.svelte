<script>
import { browser } from "$app/environment";
import { page } from "$app/stores";

export let filter;
// based on the query_param_key we can know if there is already a filter for this field
let query_param_key = filter.query_param_key;
let query_param_value_equal = get_value_from_query_param(query_param_key);
let query_param_value_lte = get_value_from_query_param(query_param_key + "_lte");
let query_param_value_gte = get_value_from_query_param(query_param_key + "_gte");
let selected_option = query_param_value_equal ? "equal" : query_param_value_lte ? "lte" : query_param_value_gte ? "gte" : "equal";
let bineded_value = query_param_value_equal || query_param_value_lte || query_param_value_gte;
function get_value_from_query_param(key) {
  return $page.url.searchParams.get(key);
}

function handle_input(event) {
  setTimeout(() => {
    $page.url.searchParams.delete(query_param_key);
    $page.url.searchParams.delete(query_param_key + "__lte");
    $page.url.searchParams.delete(query_param_key + "__gte");
    let new_val = bineded_value;

    if (selected_option === "equal") {
      $page.url.searchParams.set(query_param_key, new_val);
    } else if (selected_option === "lte") {
      $page.url.searchParams.set(query_param_key + "__lte", new_val);
    } else if (selected_option === "gte") {
      $page.url.searchParams.set(query_param_key + "__gte", new_val);
    }
  }, 0);
}
</script>

<div class="form-group">
  <div class="row">
    <div class="col">
      <select bind:value={selected_option} class="form-control" on:change={handle_input}>
        <option value="equal">שווה</option>
        <option value="lte">קטן מ</option>
        <option value="gte">גדול מ</option>
      </select>
    </div>
    <div class="col">
      {#if selected_option === "equal"}
        <input type="text" bind:value={bineded_value} on:input={handle_input} class="form-control" />
      {:else if selected_option === "lte"}
        <input type="text" bind:value={bineded_value} on:input={handle_input} class="form-control" />
      {:else if selected_option === "gte"}
        <input type="text" bind:value={bineded_value} on:input={handle_input} class="form-control" />
      {/if}
    </div>
  </div>
</div>
