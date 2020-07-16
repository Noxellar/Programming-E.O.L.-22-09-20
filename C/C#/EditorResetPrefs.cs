// UNITY EDITOR PREFERENCE RESET
// Good for
// * Resetting list of external code editors available so that it's clean and tidy
// * ERASING ALL MEMORY OF EXISTING EDITORS AND PROJECTS

// Create a folder named Editor inside Assets folder
// Place this script inside.
// This will generate on Edit menu an option called Reset Preferences.
// Click on Reset preferences and say "yes". This will clean all preferences and also clean External script list.

﻿using UnityEditor;
using UnityEngine;

public class EditorResetPrefs : MonoBehaviour
{
	[MenuItem("Edit/Reset Preferences")]
	static void ResetPrefs()
	{
		if (EditorUtility.DisplayDialog("Reset editor preferences?", "Reset all editor preferences? This cannot be undone.", "Yes", "No"))
		{
			EditorPrefs.DeleteAll();
		}
	}
}

