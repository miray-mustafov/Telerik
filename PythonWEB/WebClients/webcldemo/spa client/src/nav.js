import { add_action } from "./handlers.js";
import { icons } from "./icons.js";
import { showManagementView, productView } from "./products.js";
import { getJson } from "./requests.js";



export function main_nav_view(user) {
    const mainNav = document.querySelector('.main-nav')
    const ACTIONS = {
        products: 'manage-products'
    }
    mainNav.innerHTML = `
        <a href='#' data-action="${ACTIONS.products}">Products</a>
    `

    add_action(ACTIONS.products, () => showManagementView())
}


export function categories_view(user) {
    const categoriesNav = document.querySelector('nav.categories')

    getJson('categories')
        .then(res => {
            console.log(res)
            categoriesNav.innerHTML = res.map(obj => `
                <a href='#' 
                   data-action="select-category" 
                   data-category-id=${obj.category.id}
                >${obj.category.name}</a>
            `).join('')

            add_action('select-category', (e) => {
                document.querySelectorAll('nav.categories a').forEach(e => e.classList.remove('selected'))
                e.target.classList.add('selected')
                showCategoryProducts(e.target.dataset.categoryId)
            })
        })

}

/**
 * 
 * @param {number} categoryId 
 */
const showCategoryProducts = (categoryId) => {
    const mainView = document.querySelector('.main-view')

    getJson(`categories/${categoryId}`)
        .then(res =>
            mainView.innerHTML =
            res.products.map(productView).join('') ||
            `<h3>No products in this category. ${icons.sad()}</h3>`)
}