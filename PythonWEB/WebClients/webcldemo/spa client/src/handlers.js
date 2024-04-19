
const actions = new Map()
actions.set('default', () => { console.log('this action is not implemented') })

/**
 * 
 * @param {string} key 
 * @param {Function} action 
 */
export function add_action(key, action) {
    actions.set(key.toLowerCase(), action)
}

const clickable_tags = ['BUTTON', 'A']
document.addEventListener('click', (event) => {
    event.preventDefault()
    if (clickable_tags.includes(event.target.tagName) ||
        clickable_tags.includes(event.target.parentElement?.tagName)) {

        const data = event.target.dataset.action || event.target.parentElement.dataset.action || 'default'
        const action = actions.get(data.toLowerCase())

        if (action) {
            action(event)
        }
    }
})

