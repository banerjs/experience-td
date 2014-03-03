var ViewArticleApp = angular.module('ViewArticleApp', []);

ViewArticleApp.factory('ArticleService', function ($rootScope, $http, URLCONF) {
	return {
		getArticles: function() {
			var articles = [];
			$http.get(URLCONF.articles).success(function(data) {
				for (var i = 0; i < data.length; i++) {
					articles.push(data[i].fields);
				}
			});
			return articles;
		}
	};
});

ViewArticleApp.controller('ArticleViewCtrl', function ($scope, ArticleService) {
	// Initialize the controller on document load
	$scope.articles = ArticleService.getArticles();
});