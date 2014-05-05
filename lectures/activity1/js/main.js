function myFirstController($scope){
	$scope.hork = 'Garbl'; 
	
	$scope.names =["JD", "Vid", "Sean", "Scott"];

	$scope.addName = function(){
		$scope.names.push($scope.hork); //add new name to array
		$scope.hork="";					//clear input
	}

	$scope.removeName = function(deadIdx){
		$scope.names.splice(deadIdx,1);
		//remove starting at deadIdx, and remove one item
	}
}