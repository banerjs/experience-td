var EditArticleApp = angular.module('EditArticleApp', []);

EditArticleApp.factory('ArticleService', function ($rootScope, $http, URLCONF) {
	// Common article store between the 2 controllers
	var sharedArticle = null;

	return {
		getArticles: function() {							// This function makes HTTP requests
			var articles = [];								// to the server for articles
			$http.get(URLCONF.articles).success(function(data) {
				for (var i = 0; i < data.length; i++) {
					articles.push(data[i].fields);
				}
			});
			return articles;
		},
		deleteArticle: function(article_id) {				// Sends out a request to delete article.
			var url = URLCONF.remove.replace("99999999999999", article_id);
			$http.get(url).success(function(data) {
				console.log("Broadcasting message");
				$rootScope.$broadcast('clearArticle');		// Broadcast a message if successful
			});
		},
		sendArticle: function(article) {					// This function accepts articles into
			this.sharedArticle = angular.copy(article);		// the shared article store. It then
			this.provideArticle();							// sends out a signal when the store is ready
		},
		provideArticle: function() {						// This function sends out the signal
			$rootScope.$broadcast('articleReady');			// that the shared article store is ready
		},
	};
});

EditArticleApp.controller('ArticleFormCtrl', function ($scope, ArticleService) {
	$scope.article = {'quotes': []};

	// Function to set the article of the scope when the event "articleReady" is fired
	// from the service
	$scope.$on('articleReady', function() {
		$scope.article = angular.copy(ArticleService.sharedArticle);
	});

	// Function to handle the "clearArticle" signal
	$scope.$on('clearArticle', function() {
		console.log("clearing the form");
		$scope.clearForm();
	});

	// Functions to add and remove quotes from the scope
	$scope.addQuote = function() {
		$scope.article.quotes.push("");
	};

	$scope.removeQuote = function(index) {
		$scope.article.quotes.splice(index, 1);
	};

	// Function to clear the form when "Clear" is clicked
	$scope.clearForm = function() {
		$scope.article = {'quotes': []};
	};
});

EditArticleApp.controller('ArticleViewCtrl', function ($scope, ArticleService) {
	// Initialize the data sctructure stored in the controller
	$scope.articles = ArticleService.getArticles();

	// Refresh the article view when asked to do so by the signal
	$scope.$on('clearArticle', function() {
		console.log("fetching new articles");
		$scope.articles = ArticleService.getArticles();
	});

	// Define a function to publish a article to the service so that the form can
	// consume it
	$scope.publishArticle = function(article) {
		ArticleService.sendArticle(article);
	};

	// Define a function to remove an article from the scope. This sends a request
	// out to the server and then refreshes the article view
	$scope.removeArticle = function(article_id) {
		ArticleService.deleteArticle(article_id);
	};
});