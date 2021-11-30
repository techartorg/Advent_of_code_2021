// Licensed for use with Unreal Engine products only

using UnrealBuildTool;
using System.Collections.Generic;

public class AdventOfCode2021Target : TargetRules
{
	public AdventOfCode2021Target(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.V2;

		ExtraModuleNames.AddRange( new string[] { "AdventOfCode2021" } );
	}
}
