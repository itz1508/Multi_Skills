# Value Functions

All particle properties (startLife, startSpeed, startRotation, startSize, startColor,
emissionOverTime, emissionOverDistance, startTileIndex) use typed value objects.

## Value Types

| Type | JSON `type` | Fields | Description |
|------|------------|--------|-------------|
| ConstantValue | `ConstantValue` | `value: float` | Single value |
| ConstantColor | `ConstantColor` | `color: {r,g,b,a}` | Single RGBA color |
| IntervalValue | `IntervalValue` | `a: float, b: float` | Random between a and b |
| PiecewiseBezier | `PiecewiseBezier` | Control points | Bezier curve over time |
| Gradient | `Gradient` | Color stops | Color gradient over time |
| RandomColorBetweenGradient | `RandomColorBetweenGradient` | Two gradients | Random color between two gradients |

## Example

```json
{
  "startLife": { "type": "ConstantValue", "value": 5 },
  "startColor": { "type": "ConstantColor", "color": { "r": 1, "g": 1, "b": 1, "a": 1 } },
  "emissionOverTime": { "type": "ConstantValue", "value": 10 }
}
```

Source: verified from quarks.core/src/functions/ and test/JsonFiles.ts.
