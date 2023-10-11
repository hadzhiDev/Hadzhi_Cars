let brands = document.getElementById('brands')
let brands_card = document.querySelector('.brands_card')

brands_card.addEventListener('mouseover', e =>{
    brands.classList.remove('hidden')
})

brands_card.addEventListener('mouseout', e => {
    brands.classList.add('hidden')
})