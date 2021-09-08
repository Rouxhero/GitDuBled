 class Player {

	protected HashMap<Resources,int> listeResources;
	protected List<Character> listeCharacter;
	protected List<Tile> territory;
	protected int gold;
	/**
	* def
	* @return :void:
	**/
	public void deployCharac(Character character, Tile tile);

	/**
	* def
	* @return :void:
	**/
	public void harvestTerritory();

	/**
	* def
	* @return :void:
	**/
	public void feedCharac(Character character);

	/**
	* def
	* @return :void:
	**/
	public void endRound(Player player);

	/**
	* def
	* @return :int:
	**/
	public int convert(Resource resource){

		return 0;
	}

	/**
	* def
	* @return :int:
	**/
	public int getPoints(Player player){

		return 0;
	}

	/**
	* def
	* @return :void:
	**/
	public void rent(int amount);

	/**
	* def
	* @return :int:
	**/
	public int getGold(Player player){

		return 0;
	}


}