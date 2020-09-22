using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class StartMenu : MonoBehaviour
{
	public void Play()
	{
		Debug.Log("Pley Geym");
	}

	public void OpenOptions()
	{
		Debug.Log("Open Oopshuns");
	}

	public void Exit()
	{
		Application.Quit();
	}
}
