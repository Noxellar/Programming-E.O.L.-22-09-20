using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class OpenExhibit : MonoBehaviour
{
	public void Open()
	{
		this.gameObject.FindWithTag("Canvas").SetActive(true);
	}
}
