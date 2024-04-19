import { deleteRequest, getJson, updateRequest, createRequest } from "./requests.js"
import { icons } from "./icons.js"
import { add_action } from "./handlers.js";
import { findParent, formValuesToObject } from "./dom.js";

export const productView = (product) => {
    const [whole, fraction] = product.price.toFixed(2).split('.')

    return `
        <div class="product">
            <header><span class="p-name">${product.name}</span> <sup>$</sup><span class="p-price">${whole}</span><sup>${fraction}</sup></header>
            <p>${product.description}</p>
        </div>
    `
}

const manageProductView = (product, category, ACTIONS) => {
    return `
        <div class="manage-product">
            <div class="menu">
                <div class="category-badge">${category.name}</div>
            </div>
            ${productView(product)}
            <div class="menu">
                <button title="Edit product"
                        data-action="${ACTIONS.edit}"
                        data-product-id="${product.id}">
                    ${icons.edit()}
                </button>
                <button title="Delete product" 
                        data-action="${ACTIONS.delete}" 
                        data-product-id="${product.id}">
                    ${icons.delete()}
                </button>
            </div>
        </div>
    `
}

const confirmDeleting = (e) => {
    const btn = e.target.parentElement

    const ACTIONS = {
        confirmDelete: 'confirm-delete',
        declineDelete: 'decline-delete'
    }

    if (btn.nextSibling.tagName !== 'DIV') {
        const confirmation = document.createElement('div')
        confirmation.classList.add('confirmation-msg')
        confirmation.innerHTML = `
            Are you certain you want to delete? 
            <button data-product-id=${btn.dataset.productId} data-action="${ACTIONS.confirmDelete}" style="color:green; font-weight:bold; font-size: 16px">Yes</button>
            <button data-action="${ACTIONS.declineDelete}" style="color:red; font-weight:bold; font-size: 16px">No</button>`

        btn.parentElement.insertBefore(confirmation, btn.nextSibling)
    }

    add_action(ACTIONS.declineDelete,
        (e) => e.target.parentElement.remove())

    add_action(ACTIONS.confirmDelete,
        (e) => deleteRequest(`products/${e.target.dataset.productId}`)
            .then(r => (r.status === 204) && showManagementView()))
}

const formView = (product, categories, button) => `  
     <form>
        <input name="id" type="hidden" value="${product.id}" />
        <div>
            <label>Name <br>
                <input name="name" type="text" value="${product.name}">
            </label>
        </div>
        <div>
            <label>Price <br>
                <input name="price" type="text" value="${product.price}">
            </label>
        </div>
        <div>
            <label>Category <br>
                <select name="category_id" value="${product.category_id}">
                    ${categories.map(c => `
                        <option value=${c.id} 
                                ${product.category_id === c.id ? 'selected' : ''}
                        >${c.name}</option>`)}
                </select>
            </label>
        </div>
        <div>
            <label>Description <br>
                <textarea name="description">${product.description}</textarea>
            </label>
        </div>

        <div>
            ${button}
        </div>
    </form>`

const showEditView = (productId) => {
    const mainView = document.querySelector('.main-view')
    const ACTIONS = {
        back: 'back-to-management',
        edit: 'edit-product'
    }

    add_action(ACTIONS.back, () => showManagementView())
    add_action(ACTIONS.edit, (e) => {
        const formData = new FormData(findParent(e.target, 'form'))
        const product = formValuesToObject(formData)

        updateRequest(`products/${product.id}`, product)
            .then(res => res.status === 200 && showManagementView())
    })

    Promise.all([getJson(`products/${productId}`), getJson('categories')]).then(results => {
        const product = results[0]
        const categories = results[1].map(c => c.category)
        const button = `<button data-action=${ACTIONS.edit}>Confirm</button>`

        mainView.innerHTML = `
            <div class="edit-product">
                <h2 style="text-align:center">Edit Product #${product.id}</h2>
                <a data-action=${ACTIONS.back}>&larr; Back</a>
                ${formView(product, categories, button)}
            </div>
        `
    })
}

const showCreateView = () => {
    const mainView = document.querySelector('.main-view')
    const ACTIONS = {
        back: 'back-to-management',
        create: 'create-product'
    }

    add_action(ACTIONS.back, () => showManagementView())
    add_action(ACTIONS.create, (e) => {
        const formData = new FormData(findParent(e.target, 'form'))
        formData.delete('id')
        const product = formValuesToObject(formData)

        createRequest(`products`, product)
            .then(res => res.status === 201 && showManagementView())
    })

    getJson('categories').then(results => {
        const categories = results.map(c => c.category)
        const button = `<button data-action=${ACTIONS.create}>Confirm</button>`
        const newProduct = { 
            category_id: 1,
            name: '',
            description: '',
            price: 0
        }

        mainView.innerHTML = `
            <div class="edit-product">
                <h2 style="text-align:center">Create New Product</h2>
                <a data-action=${ACTIONS.back}>&larr; Back</a>
                ${formView(newProduct, categories, button)}
            </div>
        `
    })
}

export const showManagementView = () => {
    const mainView = document.querySelector('.main-view')
    const ACTIONS = {
        delete: 'delete-product',
        edit: 'go-to-edit-view',
        create: 'go-to-create-view'
    }

    Promise.all([getJson('products'), getJson('categories')])
        .then((results) => {
            const [products, categories] = results;
            const productsHtml = products.map(product => {
                const category = categories
                    .find(c => c.category.id === product.category_id)
                    .category

                return manageProductView(product, category, ACTIONS)
            }).join('')

            mainView.innerHTML = `
                <h2 style="text-align:center">Manage Products</h2>
                <div class="add-new-product">
                    <a data-action="${ACTIONS.create}">ADD NEW &rarr;</a>
                </div>
                <div>${productsHtml}</div>
            `

            add_action(ACTIONS.delete, confirmDeleting)
            add_action(ACTIONS.edit, (e) => showEditView(e.target.parentElement.dataset.productId))
            add_action(ACTIONS.create, showCreateView)
        })

}

