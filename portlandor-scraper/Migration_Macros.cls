VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Sheet1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Private Sub Worksheet_Change(ByVal Target As Range)
    Dim KeyCells As Range

    ' The variable KeyCells contains the cells that will
    ' cause an alert when they are changed.
    Set KeyCells = Range("C9:C250")
    
    If Not Application.Intersect(KeyCells, Range(Target.Address)) _
           Is Nothing Then

        ' Display a message when one of the designated cells has been
        ' changed.
        ' Place your code here.
        Range("C1") = Range(Target.Address).Value
        
       
    End If
    ActiveWorkbook.RefreshAll
    
End Sub

Private Sub Worksheet_SelectionChange(ByVal Target As Range)
    If Selection.Count = 1 Then
        If Not Intersect(Target, Range("D9:D250")) Is Nothing Then
            Call TestUpdateSubType
        End If
    End If
End Sub
