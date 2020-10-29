const masks = {
	cnpj (value) {
		return value
		.replace(/\D/g, '')
		.replace(/(\d{2})(\d)/, '$1.$2')
		.replace(/(\d{3})(\d)/, '$1.$2')
		.replace(/(\d{3})(\d)/, '$1/$2')
		.replace(/(\d{4})(\d)/, '$1-$2')
		.replace(/(-\d{2})\d+?$/, '$1')
	},


	telefone (value) {
		return value
		.replace(/\D/g, '')
		.replace(/(\d{2})(\d)/, '($1) $2')
		.replace(/(\d{4})(\d)/, '$1-$2')
		.replace(/(\d{4})-(\d)(\d{4})/, '$1$2-$3')
		.replace(/(-\d{4})\d+?$/, '$1')
	},

	agencia (value) {
		return value
		.replace(/\D/g, '')
		.replace(/(\d\d\d)(\d)+?$/, '$1-$2')
	},

	conta (value) {
		return value
		.replace(/\D/g, '')
		.replace(/(\d{2})(\d)/, '$1.$2')
		.replace(/(\d{3})(\d)+?$/, '$1-$2')
	}
}
//xx.xxx-x


document.querySelectorAll('input').forEach(($input) => {
	const field = $input.dataset.js
	$input.addEventListener('input', (e) => {
		e.target.value = masks[field](e.target.value)
	})
})