package t1.tile;


/**
*
* @author Leo lvcdb, Adrien G
*/

 class Desert implements Tile {

	protected static  int REWARD_COEF;

	protected  String STRING_PICT;

	protected static  int SIZE_COEF;

	protected static  int MAX_SIZE;

	protected static  int END_REWARD;


	/**
	* //TODO
	*
	* @return :void:
	**/
 	public void Desert(int x, int y) ;

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
 	public int getMaxSize() {

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
 	public int getRewardCoef() {

		return 0;
	}

	/**
	* //TODO
	*
	* @return :Ressources:
	**/
 	public Ressources getHarvest() {

		return new Ressources() ;
	}

	/**
	* //TODO
	*
	* @return :String:
	**/
 	public String toString() {

		return "";
	}


}