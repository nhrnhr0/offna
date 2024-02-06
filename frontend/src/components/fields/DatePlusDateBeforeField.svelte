<script>
import { timeduration_to_hebrew_string } from "$lib/utils";

export let key;
export let record;
export let field_options;
</script>

<!-- display the date in israel format -->
<td>
  <div class="number-field">
    {new Date(record[key]).toLocaleDateString("he-IL")}
    <div class="time-elapsed">
      <!-- now - value --> לפני ({timeduration_to_hebrew_string(new Date() - new Date(record[key]))})
    </div>
  </div></td
>
