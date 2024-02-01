<script>
// links, products, categories, orders, sizes, colors
export let links = [
  { name: "Dashboard", link: "/dashboard" },
  { name: "Products", link: "/dashboard/products", icon: "fas fa-box-open" },
  { name: "Categories", link: "/dashboard/categories", icon: "fas fa-list" },
  { name: "Orders", link: "/dashboard/orders", icon: "fas fa-shopping-cart" },
  { name: "מידות", link: "/dashboard/sizes", icon: "fas fa-ruler-combined" },
  { name: "קבוצות מידות", link: "/dashboard/size_groups", icon: "fas fa-ruler-combined" },
  { name: "Colors", link: "/dashboard/colors", icon: "fas fa-palette" },
];
</script>

<nav>
  <ul class="nav flex-column">
    {#each links as link}
      <li class="nav-item">
        <a class="nav-link" href={link.link}>
          <i class={link.icon}></i>
          {link.name}
        </a>
      </li>
    {/each}
  </ul>
</nav>

<style lang="scss">
nav {
  background-color: #fff;
  border-radius: 5px;
  padding: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: fit-content;
  padding: 10px;
  margin: 10px;
  height: fit-content;
  ul {
    list-style: none;
    padding: 0;
    margin: 0;
    li {
      a {
        color: #000;
        text-decoration: none;
        display: flex;
        align-items: center;
        padding: 10px;
        border-radius: 5px;
        &:hover {
          background-color: #f5f5f5;
        }
        i {
          margin-inline-end: 10px;
        }
      }
      ul {
        list-style: none;
        padding: 0;
        margin: 0;
        li {
          a {
            color: #000;
            text-decoration: none;
            display: flex;
            align-items: center;
            padding: 10px;
            border-radius: 5px;
            &:hover {
              background-color: #f5f5f5;
            }
            i {
              // margin-inline-end: 10px;
            }
          }
        }
      }
    }
  }
}
</style>
