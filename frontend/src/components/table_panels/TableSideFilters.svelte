<script>
import * as Types from "./../../lib/types.js";

import TextField from "../fields/TextField.svelte";
import MultiSelectFilter from "../filters/MultiSelectFilter.svelte";
import NumberFilter from "../filters/NumberFilter.svelte";
import TextFilter from "../filters/TextFilter.svelte";
import { page } from "$app/stores";
import { goto } from "$app/navigation";
import { createEventDispatcher } from "svelte";
import Modal from "../commen/Modal.svelte";
import DragDropList from "../commen/DragDropList.svelte";
import DateFilter from "../filters/DateFilter.svelte";
import { writable } from "svelte/store";

let showModal = false;

export let side_filters;
/**
 * @type {Types.FieldsOption[] | undefined}
 */
export let fields_options;
/**
 * @type {Types.FieldsOption[] | undefined}
 */
export let display_fields_options;
// $: {
//   $userPreferenceProductsTable = display_fields_options;
// }
let dispatch = createEventDispatcher();
</script>

<div class="table-settings">
  <button on:click={() => (showModal = true)}>
    <!-- settings fa icon -->
    <i class="fas fa-cog"></i>
  </button>

  <Modal bind:showModal>
    <div slot="header">
      <h2 class="modal-title">הגדרות</h2>
    </div>
    <!-- card -->
    <!-- list of all the fields and to the side anoher list of all the display fields -->
    <div class="modal-content">
      <div class="card">
        <div class="card-header">
          <h3>הצגת שדות</h3>
        </div>
        <div class="card-body">
          <div class="row">
            <div class="col">
              <div class="area-title">
                <div class="title">
                  שדות להצגה
                  <a
                    href="#"
                    on:click={(e) => {
                      e.preventDefault();
                      if (display_fields_options.length > 1) {
                        display_fields_options = [display_fields_options[0]];
                      }
                    }}>נקה</a
                  >
                </div>
              </div>
              {#if display_fields_options !== undefined}
                <DragDropList
                  bind:data={display_fields_options}
                  removesItems={true}
                  on:remove={(e) => {
                    // let idx = e.detail.index;
                    // if (display_fields_options.length > 1) {
                    //   display_fields_options = display_fields_options.filter((_, i) => i !== idx);
                    // }
                  }}
                >
                  <div slot="item" let:label>
                    <div class="list-group">
                      {label}
                    </div>
                  </div>
                </DragDropList>
              {/if}
            </div>
            <div class="col">
              <div class="area-title">
                <div class="title">
                  כל השדות
                  <a
                    href="#"
                    on:click={(e) => {
                      e.preventDefault();
                      display_fields_options = fields_options;
                    }}>הצג הכל</a
                  >
                </div>
              </div>
              <ul class="list-group">
                {#if fields_options}
                  {#each fields_options as field}
                    <button
                      class:selected={display_fields_options.find((item) => item.label === field.label) !== undefined}
                      on:click={() => {
                        if (display_fields_options.find((item) => item.label === field.label) !== undefined) {
                          display_fields_options = display_fields_options.filter((item) => item.label !== field.label);
                        } else {
                          display_fields_options = [...display_fields_options, field];
                        }
                      }}
                    >
                      {field.label}
                    </button>
                  {/each}
                {/if}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Modal>

  <h4>מיונים</h4>
  <form on:submit={(e) => e.preventDefault()}>
    {#if side_filters.length === 0}
      <p>No filters</p>
    {/if}
    {#each side_filters as filter}
      <fieldset class="form-card">
        <legend>{filter.label}</legend>
        {#if filter.type === "text"}
          <TextFilter {filter}></TextFilter>
        {:else if filter.type === "number"}
          <NumberFilter {filter}></NumberFilter>
        {:else if filter.type === "multiselect"}
          <MultiSelectFilter {filter}></MultiSelectFilter>
        {:else if filter.type === "date"}
          <DateFilter {filter}></DateFilter>
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
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.modal-title {
  display: flex;
}
.title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  a {
    color: #007bff;
    text-decoration: none;
    &:hover {
      text-decoration: underline;
    }
  }
}
.modal-content {
  min-width: 700px;
  .list-group {
    list-style: none;
    padding: 0;
    button {
      padding: 0.5rem;
      margin: 0.5rem;
      border: 1px solid #ccc;
      border-radius: 5px;
      cursor: pointer;
      text-align: right;
      &:hover {
        background-color: #f0f0f0;
      }

      &.selected {
        background-color: #d8d7d7;
      }
    }
  }
}
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
