<template>
	<v-container fluid class="pa-0">
		<v-layout row wrap align-center>
			<v-flex xs12 sm6>
				<div class="text-xs-center">
					<div>
						<button @click="deleteSuccess" color="primary" dark
							>Delete with Success</button
						>
					</div>
					<div>
						<button small @click="deleteError" color="primary" dark
							>Delete with Error</button
						>
					</div>
					<div>
						<button small @click="deleteNoSnack" color="primary" dark
							>Delete w/o Confirm & Snackbar</button
						>
					</div>
				</div>
			</v-flex>
		</v-layout>
	</v-container>
</template>

<script>
export default {
	name: 'hello-world',
	data() {
		return {
			msg: 'Welcome to Your Vue.js App'
		};
	},
	methods: {
		async deleteSuccess() {
			if (
				await this.$root.$confirm(
					'Delete?',
					'Are you sure you want to delete with success?',
					{ color: 'red' }
				)
			) {
				this.$root.$dialogLoader.start(
					'Deleting...',
					{},
					() => {
						return new Promise((resolve, reject) => {
							setTimeout(() => {
								resolve();
								// reject( 'Unable to remove client!' )
							}, 3000);
						});
					},
					true
				);
			}
		},
		async deleteError() {
			if (
				await this.$root.$confirm(
					'Delete?',
					'Are you sure you want to delete with error?',
					{ color: 'red' }
				)
			) {
				this.$root.$dialogLoader.start(
					'Deleting...',
					{},
					() => {
						return new Promise((resolve, reject) => {
							setTimeout(() => {
								//resolve()
								reject('Error deleting!');
							}, 3000);
						});
					},
					true
				);
			}
		},
		deleteNoSnack() {
			this.$root.$dialogLoader.start('Deleting...no snacks 4 u...', {}, () => {
				return new Promise((resolve, reject) => {
					setTimeout(() => {
						//resolve()
						reject('Error deleting!');
					}, 3000);
				});
			});
		}
	}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
	font-weight: normal;
}
ul {
	list-style-type: none;
	padding: 0;
}
li {
	display: inline-block;
	margin: 0 10px;
}
a {
	color: #42b983;
}
</style>
