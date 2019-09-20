{
	// here we define a variable for record keeping
	distances : [],	
	// function called at the beginning of each simulation
	setupSimulation: function() {
		this.startPos = this.getRobot().getCoreComponent().getRootPosition();
		return true;
	},

	// function called at the end of each simulation
	endSimulation: function() {

		// Compute robot ending position from its closest part to the start pos
		var minDistance = Number.MAX_VALUE;
	    	
        	bodyParts = this.getRobot().getBodyParts();
  		console.log(bodyParts.length + " body parts");
		for (var i = 0; i < bodyParts.length; i++) {
  	  		var xDiff = (bodyParts[i].getRootPosition().x - this.startPos.x);
	  		var yDiff = (bodyParts[i].getRootPosition().y - this.startPos.y);
			var dist = Math.sqrt(Math.pow(xDiff,2) + Math.pow(yDiff,2));
            		if (dist < minDistance) {
				minDistance = dist;
			}
		}
	
		this.distances.push(minDistance);
		return true;
	},


	// here we return minimum distance travelled across evaluations
	getFitness: function() {
		fitness = this.distances[0];
    		for (var i = 1; i < this.distances.length; i++) {
			if (this.distances[i] < fitness)
				fitness = this.distances[i];
		}
     		return fitness;
	},

}