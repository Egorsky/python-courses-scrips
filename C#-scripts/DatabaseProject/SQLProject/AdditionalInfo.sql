CREATE TABLE [dbo].[AdditionalInfo]
(
	[PersonId] INT NOT NULL PRIMARY KEY, 
    [Email] VARCHAR(50) NULL, 
    [NumerOfPets] NCHAR(10) NULL, 
    CONSTRAINT [FK_AdditionalInfo_ToTable] FOREIGN KEY ([PersonId]) REFERENCES [PersonalData]([PersonId])
)
