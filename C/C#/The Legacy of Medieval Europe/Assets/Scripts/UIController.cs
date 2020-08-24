using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;

public class UIController : MonoBehaviour
{
	// Player Transform variable declaration
	Transform visionPosition;

	void Awake()
	{
		visionPosition = Camera.main.transform;
	}

	public void Select(InputAction.CallbackContext ctx)
	{
		RaycastHit raycast;
		Physics.Raycast(visionPosition.position, visionPosition.TransformDirection(Vector3.forward), out raycast, 1f);

		if (raycast.collider != null)
		{
			if (raycast.collider.transform.parent.tag == "Floor Stand")
			{
				raycast.collider.transform.parent.gameObject.GetComponent<ViewExhibit>().Open();
			}
		}
	}

	public void Escape(InputAction.CallbackContext ctx)
	{
		Application.Quit();
	}
}
