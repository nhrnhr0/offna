<script>
import MultiSelect from "svelte-multiselect";
import { createEventDispatcher, onMount } from "svelte";
import { page } from "$app/stores";

export let filter;
let dispatch = createEventDispatcher();
let options;
let filter_value = [];
let is_ready = false;
$: {
  if (filter && filter.options && filter.options.length > 0) {
    options = filter.options.map((option) => {
      return { id: option.id, label: option.name };
    });
    is_ready = true;
  }
}

$: {
  if (is_ready) {
    init_from_query_param();
  }
}

function init_from_query_param() {
  if (is_ready) {
    // set the filter_value based on the query param
    let query_param_value = $page.url.searchParams.get(filter.query_param_key + "__in");

    if (query_param_value) {
      let ids = query_param_value.split(",").map((id) => parseInt(id));

      filter_value = options.filter((option) => ids.includes(option.id));
      debugger;
    } else {
      filter_value = [];
    }
  }
}
function value_changed(event) {
  //setTimeout = wait for the filter_value to be updated
  setTimeout(() => {
    //   set the query param to $page.url.searchParams
    let ids = filter_value.map((option) => option.id).join(",");
    $page.url.searchParams.set(filter.query_param_key + "__in", ids);
  }, 0);
}
</script>

<div class="form-group">
  {#if is_ready}
    <div class="text-field">
      <MultiSelect {options} placeholder="בחר..." on:change={value_changed} bind:selected={filter_value} inputClass="form-control"></MultiSelect>
    </div>
  {:else}
    <div class="text-field">
      <MultiSelect options={["ריק"]} placeholder="בחר..." inputClass="form-control"></MultiSelect>
    </div>
  {/if}
</div>
