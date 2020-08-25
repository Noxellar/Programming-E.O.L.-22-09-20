using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ViewExhibit : MonoBehaviour
{
	public void Open()
	{
		gameObject.transform.Find("Information").gameObject.SetActive(true);

		Cursor.lockState = CursorLockMode.None;
		Cursor.visible = true;
	}

	public void Close()
	{
		gameObject.transform.Find("Information").gameObject.SetActive(false);

		Cursor.lockState = CursorLockMode.Locked;
		Cursor.visible = false;
	}
}
