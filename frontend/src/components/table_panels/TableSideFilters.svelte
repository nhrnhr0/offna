<script>
import TextField from "../fields/TextField.svelte";
import MultiSelectFilter from "../filters/MultiSelectFilter.svelte";
import NumberFilter from "../filters/NumberFilter.svelte";
import TextFilter from "../filters/TextFilter.svelte";
import { page } from "$app/stores";
import { goto } from "$app/navigation";
import { createEventDispatcher } from "svelte";
import Modal from "../commen/Modal.svelte";
import DragDropList from "../commen/DragDropList.svelte";

let showModal = false;

export let side_filters;
let dispatch = createEventDispatcher();
</script>

<div class="table-settings">
  <button on:click={() => (showModal = true)}>
    <!-- settings fa icon -->
    <i class="fas fa-cog"></i>
  </button>

  <Modal bind:showModal>
    <div slot="header">
      <h2>הגדרות</h2>
    </div>
    <DragDropList data={["a", "b", "c"]} removesItems={true}></DragDropList>
  </Modal>

  <h4>מיונים</h4>
  <form on:submit={(e) => e.preventDefault()}>
    {#if side_filters.length === 0}
      <p>No filters</p>
    {/if}
    {#each side_filters as filter}
      <!-- <div class="form-card"> -->
      <!-- <label for={filter.query_param_key}>{filter.label}</label> -->
      <fieldset class="form-card">
        <legend>{filter.label}</legend>
        {#if filter.type === "text"}
          <TextFilter {filter}></TextFilter>
        {:else if filter.type === "number"}
          <NumberFilter {filter}></NumberFilter>
        {:else if filter.type === "multiselect"}
          <MultiSelectFilter {filter}></MultiSelectFilter>
        {:else}
          <p>Unknown filter type</p>
        {/if}
      </fieldset>
      <!-- </div> -->
    {/each}
    <button
      class="btn btn-primary"
      on:click={() => {
        //   redirect to $page.url;
        goto($page.url);
        dispatch("filter_updated");
      }}
      >update
    </button>
  </form>
</div>

<style lang="scss">
.table-settings {
  // direction: rtl;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border: 1px solid #ccc;

  .form-card {
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 1rem;
  }
  fieldset,
  legend {
    all: revert;
  }

  legend {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 1rem;
  }
  h4 {
    text-align: center;
    text-decoration: underline;
  }
}
</style>
