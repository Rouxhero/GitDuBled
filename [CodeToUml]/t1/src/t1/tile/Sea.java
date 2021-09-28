package t1.tile;


/**
*
* @author Leo lvcdb, Adrien G
*/

 class Sea implements Tile {

	protected static  String STRING_PICT;


	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void Sea(int x, int y) ;

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getEndCoef() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getRewardCoef() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getSizeCoef() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :int:
	**/
 	public int getMaxSize() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String toString() {

		return "";
	}

	/**
	* //TODO
	*
	* @return :Ressources:
	**/
 	public Ressources getHarvest() {

		return new Ressources() ;
	}


}