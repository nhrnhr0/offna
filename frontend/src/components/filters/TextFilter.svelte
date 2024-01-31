<script>
import { browser } from "$app/environment";
import { page } from "$app/stores";
export let filter;
// based on the query_param_key we can know if there is already a filter for this field
let query_param_key = filter.query_param_key;

let options = [
  { postfix: "__icontains", label: "מכיל" },
  { postfix: "", label: "שווה" },
];
let selected = "__icontains";
let query_param_values = {};
for (let i = 0; i < options.length; i++) {
  let option = options[i];
  let value = undefined;
  if (option.postfix === "") {
    value = get_value_from_query_param(query_param_key);
  } else {
    value = get_value_from_query_param(query_param_key + option.postfix);
  }
  query_param_values[option.postfix] = value;
  if (value) {
    selected = option.postfix;
  }
}

function handle_input(event) {
  //  set the query param to $page.url.searchParams
  for (let i = 0; i < options.length; i++) {
    let option = options[i];
    $page.url.searchParams.delete(query_param_key + option.postfix);
  }
  setTimeout(() => {
    //   set the query param to $page.url.searchParams
    let val = query_param_values[selected] || "";
    $page.url.searchParams.set(query_param_key + selected, val);
  }, 0);
  //   $page.url.searchParams.set(query_param_key + selected, query_param_values[selected]);
}
function get_value_from_query_param(key) {
  return $page.url.searchParams.get(key);
}
</script>

<div class="form-group">
  <div class="row">
    <div class="col">
      <select bind:value={selected} on:change={handle_input} class="form-control">
        {#each options as option}
          <option value={option.postfix}>{option.label}</option>
        {/each}
      </select>
    </div>
    <div class="col">
      <input type="text" bind:value={query_param_values[selected]} on:input={handle_input} class="form-control" />
    </div>
  </div>
</div>
