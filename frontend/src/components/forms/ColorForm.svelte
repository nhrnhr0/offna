<script>
import { goto } from "$app/navigation";
import { onMount } from "svelte";
import { Color } from "../../ORM/Color.js";
/**
 * @type {Object|undefined}
 */
let errors = undefined;
let loaded = false;
/**
 * @type {string|undefined}
 */
export let id = undefined;
onMount(async () => {
  if (id) {
    let clr = await Color.get(id);
    _name = clr.name;
    _color = clr.color;
    _order = clr.order;
  }
  loaded = true;
});
/**
 * @param {Event} e
 */
function handle_submit(e) {
  e.preventDefault();
  console.log("submit");
  let clr = new Color(id, _name, _color, _order);
  clr.save().then((res) => {
    debugger;
    if (!res) {
      alert("error, the server did not respond");
      return;
    } else {
      errors = undefined;
      if (res.ok) {
        // TODO: handle the different submit buttons
        let sub_val = e.submitter.value;
        res.json().then((data) => {
          let color_data = data;

          if (sub_val === "שמור") {
            goto("/dashboard/colors");
          } else if (sub_val === "שמור והוסף צבע נוסף") {
            reset_form();
            goto("/dashboard/colors/new");
          } else if (sub_val === "שמור והמשך לערוך") {
            goto(`/dashboard/colors/${color_data.id}/edit`);
          }
        });
      } else {
        res.json().then((_errors) => {
          errors = _errors;
        });
      }
    }
  });
}

onMount(() => {
  reset_form();
});

function reset_form() {
  _name = "";
  _color = "#000000";
  _order = undefined;
}

/**
 * @type {string|undefined}
 * */
let _name;
/**
 * @type {string|undefined}
 * */
let _color = "#000000";
/**
 * @type {number|undefined}
 * */
let _order;
</script>

<div class="container mt-4">
  <div class="card">
    <div class="card-header">
      <h3>
        {id ? "ערוך צבע (ID:" + id + ")" : "צבע חדש"}
      </h3>
    </div>
    <div class="card-body">
      {#if !loaded}
        <div class="spinner-border" role="status">
          <span class="sr-only">Loading...</span>
        </div>
      {:else}
        <form action="" method="post" on:submit={handle_submit}>
          <div class="form-group">
            <label for="name">שם</label>
            <input type="text" class="form-control" id="name" name="name" bind:value={_name} />
            {#if errors && errors["name"]}
              <div class="alert alert-danger" role="alert">
                {errors["name"]}
              </div>
            {/if}
          </div>
          <div class="form-group">
            <label for="color">צבע</label>
            <input type="color" class="form-control" id="color" name="color" bind:value={_color} />
            {#if errors && errors["color"]}
              <div class="alert alert-danger" role="alert">
                {errors["color"]}
              </div>
            {/if}
          </div>
          <div class="form-group">
            <label for="order">סדר</label>
            <input type="number" class="form-control" id="order" name="order" bind:value={_order} />
          </div>
          <button type="submit" class="btn btn-primary mt-4" value="שמור">שמור</button>
          <button type="submit" class="btn btn-primary mt-4" value="שמור והוסף צבע נוסף">שמור והוסף צבע נוסף</button>
          <button type="submit" class="btn btn-primary mt-4" value="שמור והמשך לערוך">שמור והמשך לערוך</button>
        </form>
      {/if}
    </div>
  </div>
</div>
