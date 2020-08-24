using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ViewExhibit : MonoBehaviour
{
	public void Open()
	{
		gameObject.transform.Find("Information").gameObject.SetActive(true);
	}

	public void Close()
	{
		gameObject.transform.Find("Information").gameObject.SetActive(false);
	}
}
