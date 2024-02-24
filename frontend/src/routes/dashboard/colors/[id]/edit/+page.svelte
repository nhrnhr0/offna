<script>
import ColorForm from "../../../../../components/forms/ColorForm.svelte";
import { page } from "$app/stores";
import { onMount } from "svelte";

let id = $page.params.id;
</script>

<ColorForm {id} />
